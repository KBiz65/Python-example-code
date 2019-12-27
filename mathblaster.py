# generate random integer values
from random import seed
from random import randint

#creating the welcome message
def welcome(user_name=None):
    if user_name != None:
        return user_name
    else:
        input("Welcome to MathBlaster 2020. Press <ENTER> to continue: ")
        print("Ok, let's get blasting!")
        user_name = input("Type your name and press <ENTER>: ")
        print("Hi, {}, welcome to MathBlaster 2020!".format(user_name))
        return user_name


def goodbye(user_name):
    print("Thank you for playing MathBlaster 2020! See you soon, {}!".format(user_name))


def get_difficulty():
    #get the user's desired difficulty level
    difficulty_level = input("""
    What difficulty level would you like to choose? Type the corresponding number to your choice.
        1. Beginner (very easy)
        2. Novice (medium difficulty)
        3. Expert (hard)
        4. Genius (extremely hard)
        difficulty: """)

    while not difficulty_level.isdigit():
        print("You must enter a number between 1 and 4 to continue.")
        difficulty_level = input("""
        What difficulty level would you like to choose? Type the corresponding number to your choice.
            1. Beginner (very easy)
            2. Novice (medium difficulty)
            3. Expert (hard)
            4. Genius (extremely hard)
            difficulty: """)

    #check if difficulty_level is <1 >4 or not an integer
    difficulty_level = int(difficulty_level)
    if (difficulty_level < 1) or (difficulty_level > 4) or not (isinstance(difficulty_level, int)):
        return get_difficulty()
    else:
        return difficulty_level


def get_function():
    chosen_function = input("""
    What function would you like to play? Type the corresponding number to your choice.
         1: Addition
         2: Subtraction
         3: Multiplication
         4: Division
    function: """)

    while not chosen_function.isdigit():
        print("You must enter a number between 1 and 4 to continue.")
        chosen_function = input("""
        What function would you like to play? Type the corresponding number to your choice.
             1: Addition
             2: Subtraction
             3: Multiplication
             4: Division
        function: """)

    #check if chosen_function is <1 >4 or not an integer
    chosen_function = int(chosen_function)
    if (chosen_function < 1) or (chosen_function > 4) or not (isinstance(chosen_function, int)):
        return print("Enter a number between 1 and 4."), get_function()
    else:
        return chosen_function


def random_x_y_generator(difficulty_level):
    # seed random number generator
    if difficulty_level == "Beginner":
        value_x = randint(0, 10)
        value_y = randint(0, 10)
        return value_x, value_y

    if difficulty_level == "Novice":
        value_x = randint(0, 100)
        value_y = randint(0, 100)
        return value_x, value_y

    if difficulty_level == "Expert":
        value_x = randint(0, 1000)
        value_y = randint(0, 1000)
        return value_x, value_y

    if difficulty_level == "Genius":
        value_x = randint(0, 1000000)
        value_y = randint(0, 1000000)
        return value_x, value_y


def questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name):
    value_x = 0
    value_y = 0

    #questions for addition
    if chosen_function == "Addition":

        while num_correct < 20 and num_wrong < 3:
            value_x, value_y = random_x_y_generator(difficulty_level)
            user_answer = input("Question {}: {} + {} = ".format(question_num, value_x, value_y))
            while not user_answer.isdigit():
                print("You need to enter a number for your answer. Let's try this again.")
                user_answer = input("Question {}: {} + {} = ".format(question_num, value_x, value_y))
            if int(user_answer) == value_x + value_y:
                num_correct += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)
            if int(user_answer) != value_x  + value_y:
                num_wrong += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)

        yes_or_no = input("""
        GAME OVER!

        You ended the game with {} correct and {} wrong. Care to try again, {}? (y/n):
        """.format(num_correct, num_wrong, user_name))

        if yes_or_no == 'y':
            play_game(user_name)
        else:
            goodbye(user_name)

    #questions for subtraction
    if chosen_function == "Subtraction":

        while num_correct < 20 and num_wrong < 3:
            value_x, value_y = random_x_y_generator(difficulty_level)
            if value_x < value_y:
                value_x, value_y = value_y, value_x
                user_answer = input("Question {}: {} - {} = ".format(question_num, value_x, value_y))
                while not user_answer.isdigit():
                    print("You need to enter a number for your answer. Let's try this again.")
                    user_answer = input("Question {}: {} - {} = ".format(question_num, value_x, value_y))

            else:
                user_answer = input("Question {}: {} - {} = ".format(question_num, value_x, value_y))
                while not user_answer.isdigit():
                    print("You need to enter a number for your answer. Let's try this again.")
                    user_answer = input("Question {}: {} - {} = ".format(question_num, value_x, value_y))

            if int(user_answer) == value_x - value_y:
                num_correct += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)
            if int(user_answer) != value_x  - value_y:
                num_wrong += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)

        yes_or_no = input("""
        GAME OVER!

        You ended the game with {} correct and {} wrong. Care to try again, {}? (y/n):
        """.format(num_correct, num_wrong, user_name))

        if yes_or_no == 'y':
            play_game(user_name)
        else:
            goodbye(user_name)

    #questions for multiplication
    if chosen_function == "Multiplication":
        while num_correct < 20 and num_wrong < 3:
            value_x, value_y = random_x_y_generator(difficulty_level)
            user_answer = input("Question {}: {} * {} = ".format(question_num, value_x, value_y))
            while not user_answer.isdigit():
                print("You need to enter a number for your answer. Let's try this again.")
                user_answer = input("Question {}: {} * {} = ".format(question_num, value_x, value_y))
            if int(user_answer) == value_x * value_y:
                num_correct += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)
            if int(user_answer) != value_x * value_y:
                num_wrong += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)
        yes_or_no = input("""
        GAME OVER!

        You ended the game with {} correct and {} wrong. Care to try again, {}? (y/n):
        """.format(num_correct, num_wrong, user_name))
        if yes_or_no == 'y':
            play_game(user_name)
        else:
            goodbye(user_name)

    #questions for division
    if chosen_function == "Division":
        while num_correct < 20 and num_wrong < 3:
            value_x, value_y = random_x_y_generator(difficulty_level)
            #checking to make sure value_y isn't 0
            if (value_y == 0):
                value_y += 1

            value_x = value_x * value_y
            user_answer = input("Question {}: {} / {} = ".format(question_num, value_x, value_y))
            while not user_answer.isdigit():
                print("You need to enter a number for your answer. Let's try this again.")
                user_answer = input("Question {}: {} / {} = ".format(question_num, value_x, value_y))
            if int(user_answer) == value_x // value_y:
                num_correct += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)
            if int(user_answer) != value_x // value_y:
                num_wrong += 1
                question_num += 1
                return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)

        yes_or_no = input("""
        GAME OVER!

        You ended the game with {} correct and {} wrong. Care to try again, {}? (y/n):
        """.format(num_correct, num_wrong, user_name))
        if yes_or_no == 'y':
            play_game(user_name)
        else:
            goodbye(user_name)


def play_game(user_name=None):
    user_name = welcome(user_name)
    chosen_function = get_function()
    difficulty_level = get_difficulty()
    num_correct = 0
    num_wrong = 0
    question_num = 1

    if chosen_function == 1:
        chosen_function = "Addition"
    elif chosen_function == 2:
        chosen_function = "Subtraction"
    elif chosen_function == 3:
        chosen_function = "Multiplication"
    else:
        chosen_function = "Division"

    if difficulty_level == 1:
        difficulty_level = "Beginner"
    elif difficulty_level == 2:
        difficulty_level = "Novice"
    elif difficulty_level == 3:
        difficulty_level = "Expert"
    else:
        difficulty_level = "Genius"

    print ("Ok, {}. Let's do some {} on {} difficulty.".format(user_name, chosen_function, difficulty_level))
    input("""
    You'll keep answering questions until you get 3 wrong or until you get 20 correct.
    Hit <ENTER> when you're ready!
    """)

    return questions(difficulty_level, chosen_function, question_num, num_correct, num_wrong, user_name)

    yes_or_no = input("""
    GAME OVER!

    You ended the game with {} correct and {} wrong. Care to try again, {}? (y/n):
    """.format(num_correct, num_wrong, user_name))
    if yes_or_no == 'y':
        play_game(user_name)
    else:
        goodbye(user_name)


seed(a = None, version = 2)
play_game()
