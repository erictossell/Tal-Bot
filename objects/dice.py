import random   

class Dice:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        if self.num_sides < 1:
            return "Please enter a number greater than 0."
        else:
            roll_result = random.randint(0, self.num_sides)
            return f"You rolled a {roll_result} (between 0 and {self.num_sides})."