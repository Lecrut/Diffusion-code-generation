import sys
class InheritanceComparator:
    def compare_mro(self, class_a, class_b) -> dict:
        mro_a = type(class_a).__mro__
        mro_b = type(class_b).__mro__
        common_prefix_length = 0
        min_len = len(mro_a) if len(mro_a) < len(mro_b) else len(mro_b)
        for i in range(min_len):
            if not (i <= common_prefix_length and mro_a[i] == mro_b[i]):
                break
            common_prefix_length += 1
        return {
            "class_a_mro": [c.__name__ for c in mro_a],
            "class_b_mro": [c.__name__ for c in mro_b],
            "common_ancestors_count": common_prefix_length,
            "first_divergence_class_a_name" if len(mro_a) > 1 else None: (mro_a[0].__name__),
            "first_divergence_class_b_name" if len(mro_b) > 1 else None: (mro_b[0].__name__),
        }
def main():
    class BaseA:
        def method(self): return "Base A"
    class MiddleB(BaseA):
        pass
    class DerivedC(MiddleB, object):
        pass
    comparator = InheritanceComparator()
    result = comparator.compare_mro(DerivedC, DerivedC)
    print("=== MRO Comparison Report ===")
    for key in sorted(result.keys()):
        value = result[key]
        if isinstance(value, list):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value}")
if __name__ == '__main__':
    main()