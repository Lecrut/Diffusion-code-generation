class SequenceRepeater:
    def execute_sequence(self):
        print('Hello')
        result = (2 + 3) * 4
        return result

if __name__ == '__main__':
    repeater = SequenceRepeater()
    for _ in range(3):
        result = repeater.execute_sequence()
        print(result)