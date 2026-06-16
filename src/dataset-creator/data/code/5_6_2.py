import sys
class InheritanceAnalyzer:
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
                    if not hasattr(type(current_class), "__subclasses__") or len([c for c in type(current_class).__subclasses__()]) == 0 and bases != [type]:
                        break
                    next_bases = []
                    for base in current_class.__bases__:
                        if isinstance(base, tuple):
                            next_bases.extend(base)
                        else:
                            next_bases.append(base)
                    break
                return mro_list
            except Exception as e:
                print(f"Error analyzing {cls}: {e}", file=sys.stderr)
                sys.exit(1)
    def compare_hierarchies(self, cls_a, cls_b):
        try:
            if not isinstance(cls_a, type) or not isinstance(cls_b, type):
                raise TypeError("Both inputs must be classes")
            mro_a = self.get_mro(cls_a)
            mro_b = self.get_mro(cls_b)
            common_prefix_len = 0
            for i in range(min(len(mro_a), len(mro_b))):
                if mro_a[i] == mro_b[i]:
                    common_prefix_len += 1
                else:
                    break
            diff_points = []
            for i in range(len(mro_a)):
                if i >= len(mro_b):
                    diff_points.append((i, "B ends here", mro_a[i]))
                    break
                class_name_a = mro_a[i].__name__
                class_name_b = mro_b[i].__name__
                if class_name_a != class_name_b:
                    pass
            return {
                "class_a_mro": [c.__name__ for c in mro_a],
                "class_b_mro": [c.__name__ for c in mro_b],
                "common_prefix_length": common_prefix_len,
                "first_divergence_index_in_a": len(mro_a) if not any(c != class_name_a and i < len(mro_a)-1 for i,c in enumerate(mro_a)) else None                                                                                  
            }
        except Exception as e:
            print(f"Error comparing {cls_a} vs {cls_b}: {e}", file=sys.stderr)
if __name__ == '__main__':
    class BaseA:
        pass
    class MiddleA(BaseA):
        def method(self): return "Middle A"
    class LeafA(MiddleA):
        pass
    class BaseB:
        pass
    class MiddleB(BaseB):
        def method(self): return "Middle B"
    class LeafB(MiddleB, BaseA):                              
        pass
    analyzer = InheritanceAnalyzer()
    result_a_b = analyzer.compare_hierarchies(LeafA, LeafB)
    print("Comparison Result:")
    for key in ["class_a_mro", "common_prefix_length"]:
        if key in result_a_b:
            val = result_a_b[key]
            if isinstance(val, list):
                print(f"{key}: {val}")
            else:
                print(f"{key}: {val}")