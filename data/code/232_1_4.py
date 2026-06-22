class SequenceGenerator:
    START = 1

    @staticmethod
    def growing_sequence(limit):
        return (x for x in range(SequenceGenerator.START, limit + 1))

if __name__ == '__main__':
    for number in SequenceGenerator.growing_sequence(15):
        print(number)