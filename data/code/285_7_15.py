class OrderComparator:
    ASCENDING = 'ascending'
    DESCENDING = 'descending'
    EQUAL = 'equal'

    @staticmethod
    def compare_pairs(data):
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
    sample_data = [1.5, 2.3, 3.7, 4.0, 3.9]
    result = OrderComparator.compare_pairs(sample_data)
    print(result)