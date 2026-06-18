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
                print(f"Error analyzing {cls}: {e}")
                sys.exit(1)
    def compare_mros(self, cls_a, cls_b):
        try:
            mro_a = self.get_mro(cls_a)
            mro_b = self.get_mro(cls_b)
            if len(mro_a) != len(mro_b):
                return {
                    "match": False,
                    "mro_a_length": len(mro_a),
                    "mro_b_length": len(mro_b),
                    "details": f"MRO lengths differ: Class A has {len(mro_a)} classes, Class B has {len(mro_b)} classes."
                }
            differences = []
            for i in range(len(mro_a)):
                if mro_a[i] != mro_b[i]:
                    differences.append({
                        "index": i,
                        "class_a": mro_a[i],
                        "class_b": mro_b[i]
                    })
            return {
                "match": len(differences) == 0,
                "mro_a_length": len(mro_a),
                "mro_b_length": len(mro_b),
                "differences_count": len(differences),
                "details": differences if differences else "Method Resolution Orders are identical."
            }
        except Exception as e:
            return {
                "match": False,
                "error_message": str(e)
            }
def main():
    class BaseA:
        def method(self):
            pass
    class MiddleB(BaseA):
        def method(self):
            super().method()
    class TopC(MiddleB):
        def method(self):
            super().method()
    class BaseD:
        def other_method(self):
            pass
    class MiddleE(BaseD):
        def other_method(self):
            super().other_method()
    class TopF(MiddleE, BaseA):
        def other_method(self):
            super().other_method()
    analyzer = InheritanceAnalyzer()
    result1 = analyzer.compare_mros(TopC, MiddleB)
    print("Comparison 1 (TopC vs MiddleB):")
    if "error_message" in result1:
        print(f"Error: {result1['error_message']}")
    else:
        print(result1["details"])
    result2 = analyzer.compare_mros(TopF, TopC)
    print("\nComparison 2 (TopF vs TopC):")
    if "error_message" in result2:
        print(f"Error: {result2['error_message']}")
    else:
        print(result2["details"])
if __name__ == '__main__':
    main()