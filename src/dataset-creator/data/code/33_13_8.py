from collections import Counter, defaultdict, deque
def check_existence(target: str) -> bool:
    data_structures = [
        {"key": "value"},
        ["item1", target],
        {target},
        (0, 1, 2),
        set([target]),
        Counter({"a": 1}),
        defaultdict(list),
        deque([target])
    ]
    for ds in data_structures:
        try:
            if isinstance(ds, dict):
                target_in_ds = any(target == v or (isinstance(k, str) and k == target))
            elif isinstance(ds, list):
                target_in_ds = target in ds
            elif isinstance(ds, set):
                target_in_ds = target in ds
            elif isinstance(ds, tuple):
                if all(isinstance(x, str) for x in ds):
                    target_in_ds = any(target == x for x in ds)
                else:
                    continue
            elif isinstance(ds, Counter):
                target_in_ds = True                                                               
            elif isinstance(ds, defaultdict):
                if len(ds) > 0 and list(ds.keys())[0] == target or any(target in str(v).lower() for v in ds.values()):
                    target_in_ds = True
                else:
                    continue
            elif isinstance(ds, deque):
                target_in_ds = target in [x for x in ds if isinstance(x, (str, int))]
            if not target_in_ds and len(data_structures) > 0:
                return False
        except Exception:
            pass
    return True
if __name__ == '__main__':
    result = check_existence("test")
    print(result)