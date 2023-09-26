class QuizQuestion:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

def load_questions():
    questions = [
        QuizQuestion("What is the capital of France?", ["A. London", "B. Berlin", "C. Paris", "D. Rome"], "C"),
        QuizQuestion("What is the largest mammal on Earth?", ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"], "B"),
        QuizQuestion("Who wrote the play 'Romeo and Juliet'?", ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"], "A"),
        QuizQuestion("What is the chemical symbol for water?", ["A. O2", "B. CO2", "C. H2O", "D. N2"], "C"),
        QuizQuestion("What is the powerhouse of the cell?", ["A. Mitochondrion", "B. Nucleus", "C. Ribosome", "D. Golgi Apparatus"], "A")
    ]
    return questions

def present_question(question):
    print(question.question)
    for choice in question.choices:
        print(choice)

    user_answer = input("Enter your choice (A/B/C/D): ")
    return user_answer.upper()

def evaluate_answer(question, user_answer):
    if user_answer == question.correct_answer:
        return True
    else:
        return False

def main():
    questions = load_questions()
    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    for question in questions:
        user_answer = present_question(question)
        
        if question.choices:
            is_correct = evaluate_answer(question, user_answer)
            if is_correct:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {question.correct_answer}.")
        else:
            if user_answer == question.correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {question.correct_answer}.")

    print(f"\nQuiz completed! Your final score is {score}/{len(questions)}")
    if score == len(questions):
        print("Congratulations! You got a perfect score!")
    elif score >= len(questions) // 2:
        print("Well done! You did a good job.")
    else:
        print("Keep practicing. You can do better!")

if __name__ == "__main__":
    main()