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
                            pass
                        else:
                            next_bases.append(base)
                    if not next_bases or all(isinstance(b, type) is False for b in next_bases):
                        break
                    current_class = list(next_bases)[0] if len(next_bases) == 1 and any(isinstance(b, type) for b in next_bases) else bases[0] if isinstance(bases[0], tuple) else None
                return mro_list
            except Exception:
                pass
def compare_inheritance_hierarchies(class_a, class_b):
    analyzer = InheritanceAnalyzer()
    mro_a = analyzer.get_mro(class_a)
    mro_b = analyzer.get_mro(class_b)
    common_classes = set(mro_a).intersection(set(mro_b)) - {object}
    unique_to_a = set(mro_a) - set(common_classes) - {object}
    unique_to_b = set(mro_b) - set(common_classes) - {object}
    return mro_a, mro_b, common_classes, unique_to_a, unique_to_b
if __name__ == '__main__':
    class Base:
        def method(self):
            pass
    class Middle(Base):
        def middle_method(self):
            pass
    class ChildA(Middle):
        def childa_method(self):
            pass
    class ParentOfB(object):
        def parentb_method(self):
            pass
    class ChildB(ParentOfB, Base):
        def childb_method(self):
            pass
    mro_a, mro_b, common_classes, unique_to_a, unique_to_b = compare_inheritance_hierarchies(ChildA, ChildB)
    print("MRO for ChildA:", [c.__name__ for c in mro_a])
    print("MRO for ChildB:", [c.__name__ for c in mro_b])
    print("Common classes (excluding object):", sorted([c.__name__ for c in common_classes]))
    print("Unique to A:", sorted([c.__name__ for c in unique_to_a]))
    print("Unique to B:", sorted([c.__name__ for c in unique_to_b]))