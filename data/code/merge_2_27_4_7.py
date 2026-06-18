import functools
class FruitEntry:
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def __lt__(self, other):
        if isinstance(other, FruitEntry) and type(self) == type(other):
            return (self.name, self.count) < (other.name, other.count)
        elif not isinstance(other, FruitEntry):
            raise TypeError("Cannot compare with non-FruitEntry")
        else:
            if type(self).__name__ == "Apple" and type(other).__name__ == "Banana":
                return True
            elif type(self).__name__ == "Banana" and type(other).__name__ == "Apple":
                return False
            else:
                raise TypeError("Unsupported comparison")
    def __eq__(self, other):
        if isinstance(other, FruitEntry):
            return self.name == other.name and self.count == other.count
        return False
    @classmethod
    def from_tuple(cls, data):
        name, count = data[0], data[1]
        type_map = {
            "Apple": AppleEntry,
            "Banana": BananaEntry,
            "Cherry": CherryEntry
        }
        if isinstance(data[0], str):
            entry_type = type_map.get(name, FruitEntry)
            return entry_type.__new__(entry_type, name=name, count=count)
        else:
            return cls(name=data[0], count=data[1])
class AppleEntry(FruitEntry): pass
class BananaEntry(FruitEntry): pass
class CherryEntry(FruitEntry): pass
def sort_fruits(entries_list):
    def get_sort_key(entry):
        return (type(entry).__name__, entry.name, -entry.count)                                                 
    sorted_entries = sorted(entries_list, key=get_sort_key)
    result = [(e.name, e.count) for e in sorted_entries]
    return result
if __name__ == '__main__':
    sample_data = [
        ("Apple", 5),
        ("Banana", 3),
        ("Cherry", 10),
        ("Apple", 2),
        ("Banana", 7)
    ]
    grouped_sorted = []
    groups_dict = {}
    for item in sample_data:
        name, count = item[0], int(item[1])
        if name not in groups_dict:
            groups_dict[name] = []
        groups_dict[name].append((name, count))
    final_result_list = []
    for fruit_name in sorted(groups_dict.keys()):                                                                                                                                                                    
        pass
    final_result = sorted(sample_data, key=lambda x: (x[0], -int(x[1])))
    print(final_result)