class DetermineTheLargestNumberPresentProcessor:
    MAX_VALUE = float('-inf')

    @staticmethod
    def update_max_value(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        for number in numbers:
            if number > DetermineTheLargestNumberPresentProcessor.MAX_VALUE:
                DetermineTheLargestNumberPresentProcessor.MAX_VALUE = number

    @classmethod
    def get_max_value(cls):
        return cls.MAX_VALUE

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    sample_list4 = []

    processor.update_max_value(sample_list1)
    print(f"Maximum in {sample_list1}: {processor.get_max_value()}")

    processor.update_max_value(sample_list2)
    print(f"Maximum in {sample_list2}: {processor.get_max_value()}")

    processor.update_max_value(sample_list3)
    print(f"Maximum in {sample_list3}: {processor.get_max_value()}")

    try:
        processor.update_max_value(sample_list4)
    except ValueError as e:
        print(e)

    processor.update_max_value([100])
    print(f"Maximum in [100]: {processor.get_max_value()}")