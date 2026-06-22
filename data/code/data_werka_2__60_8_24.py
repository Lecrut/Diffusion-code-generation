class StringListProcessor:
    DEFAULT_LIST = ["apple", "banana", "cherry"]

    @staticmethod
    def get_last_item(strings):
        if not isinstance(strings, list):
            raise ValueError("Input must be a list.")
        if len(strings) == 0:
            raise IndexError("The list is empty and has no last item.")
        return strings[-1]

if __name__ == '__main__':
    sample_list = StringListProcessor.DEFAULT_LIST
    try:
        last_item = StringListProcessor.get_last_item(sample_list)
        print(f"The last item in the list is: {last_item}")
    except Exception as e:
        print(e)