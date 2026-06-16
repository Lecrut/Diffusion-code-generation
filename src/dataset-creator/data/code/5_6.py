import sys
class MROAnalyzer:
    def get_mro(self, cls):
        if hasattr(cls, "__mro__"):
            return list(cls.__mro__)
        else:
            try:
                bases = [b for b in type(cls).__bases__]
                mro_list = []
                current_class = cls
                while True:
                    mro_list.append(current_class)
                    if not hasattr(type(current_class), "__subclasses__"):
                        break
                    next_bases = list(set([base for base in bases + [type(current_class).__bases__] 
                                            if id(base) != id(cls)]))
                    current_mro = []
                    visited = set()
                    def traverse(c):
                        if c not in visited:
                            visited.add(c)
                            current_mro.append(c)
                            for b in type(c).__mro__[1:-1]:
                                traverse(b)
                    traverse(current_class)
                return list(reversed(mro_list))
            except Exception as e:
                print(f"Error calculating MRO: {e}", file=sys.stderr)
                sys.exit(1)
def compare_mros(cls_a, cls_b):
    mro_a = [c.__name__ for c in cls_a.__mro__]
    mro_b = [c.__name__ for c in cls_b.__mro__]
    common_prefix_len = 0
    while common_prefix_len < len(mro_a) and common_prefix_len < len(mro_b):
        if mro_a[common_prefix_len] == mro_b[common_prefix_len]:
            common_prefix_len += 1
        else:
            break
    diff_indices_mro_a = list(range(common_prefix_len, len(mro_a)))
    diff_indices_mro_b = list(range(common_prefix_len, len(mro_b)))
    return {
        "class_a": cls_a.__name__,
        "class_b": cls_b.__name__,
        "common_ancestors_count": common_prefix_len,
        "mro_class_a": mro_a,
        "mro_class_b": mro_b,
        "first_divergence_index_mro_a": diff_indices_mro_a[0] if diff_indices_mro_a else None,
        "first_divergence_index_mro_b": diff_indices_mro_b[0] if diff_indices_mro_b else None,
    }
if __name__ == '__main__':
    class Base:
        def method(self):
            return "Base"
    class MiddleA(Base):
        pass
    class ChildAMiddle(MiddleA):
        pass
    class MiddleB(Base):
        pass
    class ChildBMiddle(MiddleB):
        pass
    analyzer = MROAnalyzer()
    result_a = compare_mros(ChildAMiddle, Base)
    print(f"Class A: {result_a['class_a']}")
    print("MRO:", " -> ".join(result_a["mro_class_a"]))
    print("\nCommon Ancestors Count:", result_a["common_ancestors_count"])
    result_b = compare_mros(ChildBMiddle, Base)
    print(f"\nClass B: {result_b['class_b']}")
    print("MRO:", " -> ".join(result_b["mro_class_b"]))
    print("\nCommon Ancestors Count:", result_b["common_ancestors_count"])
    if sys.version_info >= (3, 10):
        import inspect
        def get_mro_v3(cls):
            return [c.__name__ for c in cls.__mro__]
        print("\nPython 3.10+ MRO Check:")
        print("ChildAMiddle:", " -> ".join(get_mro_v3(ChildAMiddle)))
    else:
        print(f"\nMRO (Standard): {result_a['class_a']}")