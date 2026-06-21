class ListCombiner:
    @staticmethod
    def combine(list_alpha, list_beta):
        result = list_alpha.copy()
        result.extend(list_beta)
        return result

if __name__ == '__main__':
    sample_list1 = ["apple", "banana"]
    sample_list2 = ["cherry", "date"]
    combined_list = ListCombiner.combine(sample_list1, sample_list2)
    print(combined_list)