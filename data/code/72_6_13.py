class ListComparator:
    RELATIONSHIP_SYMBOLS = {
        "less": "<",
        "equal": "==",
        "greater": ">"
    }

    @staticmethod
    def determine_relationship(a, b):
        if a < b:
            return "less"
        if a > b:
            return "greater"
        return "equal"

    def compare(self, list_one, list_two):
        results = []
        for val_a, val_b in zip(list_one, list_two):
            rel_type = self.determine_relationship(val_a, val_b)
            symbol = self.RELATIONSHIP_SYMBOLS[rel_type]
            results.append(f"{val_a} {symbol} {val_b}")
        return results

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = [5, 20, 35]
    comparator = ListComparator()
    comparison_results = comparator.compare(first_list, second_list)
    print(comparison_results)