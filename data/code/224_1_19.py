import statistics

class ScoreCalculator:
    @staticmethod
    def calculate_mean(scores):
        if not scores:
            return 0
        return statistics.mean(scores)

if __name__ == '__main__':
    calculator = ScoreCalculator()
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = [10.5, 20.5, 30.5]
    list4 = [-1, 5, 10, -5]
    
    print(f"Mean of {list1}: {calculator.calculate_mean(list1)}")
    print(f"Mean of {list2}: {calculator.calculate_mean(list2)}")
    print(f"Mean of {list3}: {calculator.calculate_mean(list3)}")
    print(f"Mean of {list4}: {calculator.calculate_mean(list4)}")