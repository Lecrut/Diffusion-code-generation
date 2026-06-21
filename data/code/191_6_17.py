class ListCombiner:
    @staticmethod
    def combine_lists(list_alpha, list_beta):
        result = list_alpha.copy()
        result.extend(list_beta)
        return result

if __name__ == '__main__':
    list_a = ["apple", "banana"]
    list_b = ["cherry", "date"]
    combined = ListCombiner.combine_lists(list_a, list_b)
    print(combined)