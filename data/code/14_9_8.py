import threading

def safe_extract_third(lst, default=None):
    with _lock:
        if len(lst) >= 3:
            return lst[2]
        return default

_lock = threading.Lock()

def run_samples():
    samples = [
        ([1, 2, 3, 4], 3),
        ([1, 2], None),
        ([10, 20], -1),
        ([], -99),
        (["a", "b", "c", "d", "e"], "c"),
    ]
    for data, expected in samples:
        result = safe_extract_third(data, default=expected)
        print(result)

if __name__ == '__main__':
    run_samples()