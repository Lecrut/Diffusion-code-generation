import random
import hashlib

class RandomStringSelector:
    SEPARATOR = "|"
    
    @staticmethod
    def compute_hash_index(key, bounds):
        raw = f"{key}:{bounds}".encode('utf-8')
        hash_val = int(hashlib.sha256(raw).hexdigest(), 16)
        return hash_val % bounds
    
    @classmethod
    def select(cls, string_tuple, seed_value):
        random.seed(seed_value)
        if not string_tuple:
            raise ValueError("Tuple must not be empty")
        count = len(string_tuple)
        random_index = random.randint(0, count - 1)
        return string_tuple[random_index]

if __name__ == '__main__':
    data = ("red", "blue", "green", "yellow")
    s = 100
    result = RandomStringSelector.select(data, s)
    print(result)