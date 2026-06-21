def group_names_by_first_letter(names):
    grouped = {}
    for name in names:
        first_letter = name[0].upper()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(name)
    return grouped

class NameGrouper:
    def __init__(self, names):
        self.names = names
        self.grouped_names = group_names_by_first_letter(names)

    def get_grouped_names(self):
        return self.grouped_names

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    grouper = NameGrouper(sample_names)
    print(grouper.get_grouped_names())