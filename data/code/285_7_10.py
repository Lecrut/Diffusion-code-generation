class OrderComparator:
    ASCENDING = "ascending"
    DESCENDING = "descending"
    EQUAL = "equal"

    @staticmethod
    def compare_adjacent(data):
        results = []
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                results.append(OrderComparator.ASCENDING)
            elif data[i] > data[i + 1]:
                results.append(OrderComparator.DESCENDING)
            else:
                results.append(OrderComparator.EQUAL)
        return results

if __name__ == '__main__':
    sample_list = [3.5, 2.8, 4.0, 4.0, 1.2]
    result = OrderComparator.compare_adjacent(sample_list)
    print(result)