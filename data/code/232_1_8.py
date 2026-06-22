class SequenceGenerator:
    START = 1

    @staticmethod
    def growing_sequence(limit):
        return (x for x in range(SequenceGenerator.START, limit + 1))

if __name__ == '__main__':
    generator_instance = SequenceGenerator()
    for number in generator_instance.growing_sequence(25):
        print(number)