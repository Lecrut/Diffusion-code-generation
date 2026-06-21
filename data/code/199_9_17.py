class NameManipulator:
    def __init__(self, names):
        self.names = names

    def reverse_names(self):
        reversed_names = [name[::-1] for name in self.names]
        return reversed_names

    def sort_names(self):
        sorted_names = sorted(self.reverse_names())
        return sorted_names

if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
    manipulator = NameManipulator(sample_list)
    print("Original List:", sample_list)
    reversed_sorted_names = manipulator.sort_names()
    print("Reversed and Sorted Names:", reversed_sorted_names)