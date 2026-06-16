import sys
class InheritanceAnalyzer:
    def get_mro(self, cls):
        return list(cls.__mro__)
    def compare_hierarchies(self, class_a, class_b):
        mro_a = self.get_mro(class_a)
        mro_b = self.get_mro(class_b)
        common_prefix_length = 0
        for i in range(min(len(mro_a), len(mro_b))):
            if mro_a[i] == mro_b[i]:
                common_prefix_length += 1
            else:
                break
        divergence_point_class_name = None
        if common_prefix_length > 0:
            for i in range(common_prefix_length, max(len(mro_a), len(mro_b))):
                class_a_parent = mro_a[i]
                class_b_parent = mro_b[i]
                if class_a_parent != class_b_parent and not (class_a_parent == object or class_b_parent == object):
                    divergence_point_class_name = f"{class_a_parent.__name__} vs {class_b_parent.__name__}"
                    break
        return {
            "class_a_mro": mro_a,
            "class_b_mro": mro_b,
            "common_prefix_length": common_prefix_length,
            "divergence_point": divergence_point_class_name
        }
def create_sample_classes():
    class Base:
        def method(self):
            return "Base"
    class A(Base):
        def method(self):
            return f"A in {self.__class__.__name__}"
    class B(A, Base):
        pass
    class C(B):
        pass
    class D(C):
        pass
    class E:
        def method(self):
            return "E"
    class F(E):
        def method(self):
            return f"F in {self.__class__.__name__}"
    G = type('G', (B, F), {})
    classes_to_compare = [A, B]
    target_a = A
    target_b = B
    sample_classes = {"Base": Base, "A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G}
    return classes_to_compare, target_a, target_b, sample_classes
if __name__ == '__main__':
    _, class_a, class_b, _ = create_sample_classes()
    analyzer = InheritanceAnalyzer()
    result = analyzer.compare_hierarchies(class_a, class_b)
    print("Class A MRO:", [c.__name__ for c in result["class_a_mro"]])
    print("Class B MRO:", [c.__name__ for c in result["class_b_mro"]])
    print(f"Common Prefix Length: {result['common_prefix_length']}")
    if result["divergence_point"]:
        print(f"Divergence Point: {result['divergence_point']}")
    sys.exit(0)