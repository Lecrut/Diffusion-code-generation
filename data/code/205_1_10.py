class DescendingSorter:
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] < data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

if __name__ == '__main__':
    sorter = DescendingSorter()
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6]
    sorted_values = sorter.sort(sample_values)
    print(sorted_values)