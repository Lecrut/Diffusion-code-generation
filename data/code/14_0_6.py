class ThirdElementRetriever:
    MIN_LENGTH = 3

    @staticmethod
    def get_third(data):
        if len(data) < ThirdElementRetriever.MIN_LENGTH:
            raise IndexError("List has fewer than three items")
        return data[2]

if __name__ == '__main__':
    full_data = [100, 200, 300, 400]
    partial_data = [10, 20]
    
    result1 = ThirdElementRetriever.get_third(full_data)
    print(result1)
    
    try:
        result2 = ThirdElementRetriever.get_third(partial_data)
        print(result2)
    except IndexError as err:
        print(str(err))