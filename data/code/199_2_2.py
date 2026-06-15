class NameManipulator:
    def randomize_list(self, names_list):
        n = len(names_list)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            names_list[i], names_list[j] = names_list[j], names_list[i]
if __name__ == '__main__':
    import random
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    manipulator = NameManipulator()
    print("Original list:", sample_names)
    manipulator.randomize_list(sample_names)
    print("Randomized list:", sample_names)
    sample_names_2 = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
    print("\nOriginal list 2:", sample_names_2)
    manipulator.randomize_list(sample_names_2)
    print("Randomized list 2:", sample_names_2)