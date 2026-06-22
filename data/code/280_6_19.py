class ActionRepeater:
    MAX_REPETITIONS = 3

    @staticmethod
    def repeat_action(number):
        if number >= ActionRepeater.MAX_REPETITIONS:
            return "Max repetitions reached"
        
        for _ in range(number):
            print("Action performed")
        
        return f"Repeated {number} times"

if __name__ == '__main__':
    sample_input = 2
    result = ActionRepeater.repeat_action(sample_input)
    print(result)