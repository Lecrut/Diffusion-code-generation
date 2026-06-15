class NameManipulator:
    def randomize_list(self, names_list):
        n = len(names_list)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            names_list[i], names_list[j] = names_list[j], names_list[i]
if __name__ == '__main__':
    import random
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    manipulator = NameManipulator()
    print("Original list:", names)
    manipulator.randomize_list(names)
    print("Randomized list 1:", names)
    names2 = ["A", "B", "C", "D", "E", "F", "G"]
    print("Original list 2:", names2)
    manipulator.randomize_list(names2)
    print("Randomized list 2:", names2)