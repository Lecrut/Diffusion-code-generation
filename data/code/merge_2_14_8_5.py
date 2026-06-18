import hashlib
from collections import defaultdict
class DuplicateRemover:
    def remove_duplicates(self, data):
        seen = set()
        unique_data = []
        for item in data:
            if isinstance(item, (int, float)):
                key = id(item)
            elif isinstance(item, str):
                key = hash(item.encode('utf-8')) % 2**31
            else:
                try:
                    serialized = hashlib.md5(str(item).encode()).hexdigest()[:16]
                    key = int(serialized, 16)
                except Exception:
                    continue
            if key not in seen:
                seen.add(key)
                unique_data.append(item)
        return unique_data
if __name__ == '__main__':
    sample_array = [3.5, 'apple', 2, 'banana', 10, 'apple', None, True, False, 10]
    remover = DuplicateRemover()
    result = remover.remove_duplicates(sample_array)
    print(result)