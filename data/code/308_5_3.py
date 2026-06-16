class SequenceAnalyzer:
    @staticmethod
    def count_even_integers(sequence):
        count = 0
        for number in sequence:
            if number % 2 == 0:
                count += 1
        return count
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5, 6]
    data2 = [7, 8, 9, 10, 11, 12]
    data3 = [1, 3, 5, 7, 9]
    data4 = [2, 4, 6, 8, 10]
    print(SequenceAnalyzer.count_even_integers(data1))
    print(SequenceAnalyzer.count_even_integers(data2))
    print(SequenceAnalyzer.count_even_integers(data3))
    print(SequenceAnalyzer.count_even_integers(data4))