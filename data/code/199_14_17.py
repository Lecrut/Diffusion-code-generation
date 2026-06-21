class NameMerger:
    @staticmethod
    def merge_and_clean(names1, names2):
        merged_names = names1 + names2
        cleaned_names = [name.strip() for name in merged_names if name]
        unique_names = list(set(cleaned_names))
        unique_names.sort()
        return unique_names

if __name__ == '__main__':
    sample_names_1 = ["Alice", "Bob   ", "Charlie"]
    sample_names_2 = ["  David", "Betty", "Anna", "David"]
    result = NameMerger.merge_and_clean(sample_names_1, sample_names_2)
    print(result)