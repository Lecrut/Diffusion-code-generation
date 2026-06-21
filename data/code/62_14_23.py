class SecondItemRetriever:
    @staticmethod
    def get_second_item(lst):
        return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    sample_list_1 = [5, 10, 15, 20]
    sample_list_2 = ['apple', 'banana']
    sample_list_3 = [True]
    sample_list_4 = []
    
    print(SecondItemRetriever.get_second_item(sample_list_1))
    print(SecondItemRetriever.get_second_item(sample_list_2))
    print(SecondItemRetriever.get_second_item(sample_list_3))
    print(SecondItemRetriever.get_second_item(sample_list_4))