class NameGrouping:
    def group_names_by_first_letter(self, names):
        grouped = {}
        for name in names:
            first_letter = name[0].upper()
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(name)
        return grouped

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    grouping = NameGrouping()
    result = grouping.group_names_by_first_letter(sample_names)
    print(result)

    another_sample_names = ["Frank", "Grace", "Hank", "Ivy"]
    another_result = grouping.group_names_by_first_letter(another_sample_names)
    print(another_result)