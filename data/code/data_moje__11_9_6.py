import operator

class ListAccessor:
    LAST_INDEX = -1
    
    @staticmethod
    def retrieve_last(data):
        getter = operator.itemgetter(ListAccessor.LAST_INDEX)
        return getter(data)

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    result = ListAccessor.retrieve_last(sample_data)
    print(result)