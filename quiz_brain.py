class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.correct_answers = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.correct_answers += 1
            print(f"Correct")
        else:
            print(f"Incorrect")
        print(f"Your score is ({self.correct_answers}/{self.question_number}) \n")
