class OrderChecker:
    ASCENDING = 'ascending'
    DESCENDING = 'descending'
    EQUAL = 'equal'

    @staticmethod
    def check_order(data):
        results = []
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                results.append((data[i], data[i + 1], OrderChecker.ASCENDING))
            elif data[i] > data[i + 1]:
                results.append((data[i], data[i + 1], OrderChecker.DESCENDING))
            else:
                results.append((data[i], data[i + 1], OrderChecker.EQUAL))
        return results

if __name__ == '__main__':
    sample_list = [1, 3, 2, 5, 4, 6, 7]
    checker = OrderChecker()
    result = checker.check_order(sample_list)
    print(result)