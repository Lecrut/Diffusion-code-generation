MAX_ITERATIONS = 1000

class ListModifier:
    def __init__(self, initial_data=None):
        self.items = initial_data if initial_data is not None else []

    def append(self, item):
        self.items.append(item)

    def remove_all_instances(self, item_to_remove):
        iteration_count = 0
        while item_to_remove in self.items:
            index = self.items.index(item_to_remove)
            del self.items[index]
            iteration_count += 1
            if iteration_count > MAX_ITERATIONS:
                raise ValueError("Too many iterations to remove all instances")

if __name__ == '__main__':
    lm = ListModifier()
    lm.append(1)
    lm.append(2)
    lm.append(3)
    lm.append(2)
    print("Original list:", lm.items)
    lm.remove_all_instances(2)
    print("Modified list:", lm.items)