class Statistics:
    @staticmethod
    def mean(data):
        return sum(data) / len(data)

if __name__ == '__main__':
    stats = Statistics()
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [10.5, 20.5, 30.5]
    print(f"Mean of {numbers1}: {stats.mean(numbers1)}")
    print(f"Mean of {numbers2}: {stats.mean(numbers2)}")