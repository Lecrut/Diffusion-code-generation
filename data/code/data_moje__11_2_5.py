class ListAccessor:
    @staticmethod
    def get_last_element(data):
        return data[-1:][0]

if __name__ == '__main__':
    sample_data = ["red", "green", "blue", "yellow", "purple"]
    output_value = ListAccessor.get_last_element(sample_data)
    print(output_value)