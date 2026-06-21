class Sorter:
    @staticmethod
    def sort(lst):
        return sorted(lst)

if __name__ == '__main__':
    sorter = Sorter()
    print(sorter.sort([3.5, 1.2, 4.8, 2.1]))
    print(sorter.sort([3.14, 2.71, 0.57, 1.61]))
    print(sorter.sort([3.5, 1.2, 4.8, 2.9]))