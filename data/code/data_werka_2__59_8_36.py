class SequenceUtils:
    @staticmethod
    def find_middle_item(sequence):
        if len(sequence) == 0:
            raise ValueError("The sequence is empty")
        middle_index = len(sequence) // 2
        return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(SequenceUtils.find_middle_item(sample_list))
    except ValueError as e:
        print(e)