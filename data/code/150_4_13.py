class ListProcessor:
    @staticmethod
    def remove_value(input_list, value_to_remove):
        return [item for item in input_list if item != value_to_remove]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'banana']
    result = ListProcessor.remove_value(sample_list, 'banana')
    print(result)