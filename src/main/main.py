import tkinter as tk
from tkinter import messagebox

class GUI:

    def __init__(self):
      # Initialize the main GUI window
      self.window = tk.Tk()
      self.window.geometry("750x500")
      self.window.title("Main Menu")
      self.option = "This is an exam to test yourself."

      # Widgets for the main window
      self.label = tk.Label(self.window, text="Welcome to the year 13 Computer science Revision tool!", font=('Helvetica', 20))
      self.label.pack(padx=5, pady=20)

      self.display_text = tk.Label(self.window, text=self.option, font=('Helvetica', 13), justify="left")
      self.display_text.pack(padx=10, pady=10)


      button_width = 250
      button_height = 100
      button_x = (750 - button_width) // 2
      button_y = (620 - button_height) // 2

      self.button_state = tk.IntVar()
      self.button = tk.Button(self.window, text="Begin", font=('Helvetica', 15), command=self.on_opening)
      self.button.place(x=button_x, y=button_y, width=button_width, height=button_height)

      # Set up the protocol for window closing
      self.window.protocol("WM_DELETE_WINDOW", self.on_closing_gui)

    def on_opening(self):
      # Handle the "Next" button press
      if self.button_state.get() == 0:
          # Destroy the current window and open the QuizWindow
          self.window.destroy()
          QuizWindow()


    def on_closing_gui(self):
      # Handle the window closing event
      if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
          self.window.destroy()

class QuizWindow:

    def __init__(self):
        # Initialize the QuizWindow
        self.quiz_window = tk.Tk()
        self.quiz_window.geometry("750x500")
        self.quiz_window.title("Computer Science Quiz")

        # Questions and answers
        self.questions = [
            "1. A compression technique is applied to the line of data and results in the following:\n6W3B12W6B1W3B4W\nState what data compression algorithm has been applied.",
            "2. State Nyquist's Theorem.",
            "3. Define what a protocol is.",
            "4. Describe the difference between Natural numbers and Integers:",
            "5. What is a recursive function in computer science?",
            "6. What does the term 'algorithm' refer to?",
            "7. What is the primary purpose of a compiler in programming?",
            "8. What is object-oriented programming (OOP) in computer science?",
        ]

        self.answers = ["a", "b", "c", "b", "b", "c", "a", "c"]

        # Create the quiz user interface
        self.create_quiz_ui()

    def create_quiz_ui(self):
        canvas = tk.Canvas(self.quiz_window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_frame = tk.Frame(canvas)
        scroll_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas.create_window((0, 0), window=scroll_frame, anchor=tk.NW)

        scrollbar = tk.Scrollbar(self.quiz_window, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)


        for i, question_text in enumerate(self.questions):
            question_label = tk.Label(scroll_frame, text=question_text, font=('Helvetica', 12), justify="left")
            question_label.pack(padx=10, pady=10, anchor=tk.W)


        # Defines the Answer Booklet at the bottom right
        self.submit_button = tk.IntVar()
        submit_button = tk.Button(scroll_frame, text="Answer booklet", font=('Helvetica', 12), command=self.on_opening_feedback)
        submit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Defines the mark scheme button at the bottom left
        self.ms_button_state = tk.IntVar()
        ms_button = tk.Button(scroll_frame, text="Mark Scheme", font=("Helvetica", 12), command=self.on_opening_ms)
        ms_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Updates the canvas to include all elements
        canvas.update_idletasks()

        # Configures the canvas scrolling region
        canvas.config(scrollregion=canvas.bbox(tk.ALL))

        self.quiz_window.protocol("WM_DELETE_WINDOW", self.on_closing_quiz)

    # Subroutine to evaluate the answers and displays how many the user got correct
    def evaluate_answers(self, user_answers):
        # Check user answers and displays the score
        score = sum(1 for i, user_answer in user_answers.items() if user_answer.get().lower() == self.answers[i])
        messagebox.showinfo("Quiz Result", f"You got {score} out of {len(self.questions)} questions correct.")


    # Handles the closing procedure of the quiz window
    def on_closing_quiz(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self.quiz_window.destroy()

    # Handles the opening procedure of the marks scheme window
    def on_opening_ms(self):
        if self.ms_button_state.get() == 0:
            markSchWindow()

    # Handles the opening procedure of the feedback window
    def on_opening_feedback(self):
        if self.submit_button.get() == 0:
            Answer_booklet()

# Creates the page for the mark Scheme
class markSchWindow:

    def __init__(self):
        self.MS_window = tk.Tk()
        self.MS_window.geometry("700x500")
        self.MS_window.title("Mark Scheme")
        self.create_ms_ui()

    def create_ms_ui(self):
        canvas = tk.Canvas(self.MS_window)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_frame = tk.Frame(canvas)
        scroll_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas.create_window((0, 0), window=scroll_frame, anchor=tk.NW)

        scrollbar = tk.Scrollbar(self.MS_window, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)


        for j, ms_text in enumerate(self.mark_scheme):
            ms_label = tk.Label(scroll_frame, text=ms_text, font=("Helvetica", 12), justify="left")
            ms_label.pack(padx=10, pady=10, anchor=tk.W)

class Answer_booklet():

    def __init__(self):
        self.feedback_Window = tk.Tk()
        self.feedback_Window.geometry("750x520")
        self.feedback_Window.title("Feedback")
        self.topics = ["1","2","3","4","5","6","7","8"]

        self.mark_scheme = {
            "Compression": "Lossless",
            "Representing sound": "Sound recorded is twice the highest frequency",
            "Transmission Protocols": "rules or regulations that govern computer behaviour",
            "Number systems": "integers can be negative, natural numbers cannot",
            "Recursion": "a function that calls itself",
            "Fundamentals of Data Representation": "a set of instructions to solve a problem or carry out a task",
            "Types of Translators": "to translate code from high level to machine code in one go",
            "Object Oriented Programming": "programming paradigm based on objects"
        }

        self.answers = {}
        self.create_feedback_ui()



    def create_feedback_ui(self):
        for index, topic in enumerate(self.topics, start=1):
            label = tk.Label(self.feedback_Window, text=f"Answer for question {topic}",font=('Helvetica', 12), justify="left")
            label.pack(pady= 5)

            ans_entry = tk.Entry(self.feedback_Window)
            ans_entry.pack()

        submit_button = tk.Button(self.feedback_Window, text="Submit", command=self.check_answers, justify="right")
        submit_button.pack()

    def check_answers(self):
        total_questions = len(self.topics)
        correct_ans = 0
        for topic, entry in self.answers.items():
            user_ans = entry.get()
            if user_ans.lower() == self.mark_scheme.get(topic).lower():
                correct_ans += 1
        percentage = (correct_ans/total_questions)*100
        grade = self.calculate_grade(percentage)
        result_label = tk.Label(self.feedback_Window, text=f"Percentage: {percentage: .2f}%\nGrade: {grade}")
        result_label.pack()



    def calculate_grade(self, percentage):
        if percentage >= 90:
            return "A"
        elif 80 <= percentage < 90:
            return "B"
        elif 70 <= percentage < 80:
            return "C"
        elif 60 <= percentage < 70:
            return "D"
        else:
            return "E"


if __name__ == "__main__":
  # Run the main GUI
  gui = GUI()
  gui.window.mainloop()