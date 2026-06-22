class IncrementalSequence:
    def print_incremental_sequence(self):
        step = 1
        for i in range(5):
            print(step)
            step += i + 1

if __name__ == '__main__':
    sequence = IncrementalSequence()
    sequence.print_incremental_sequence()