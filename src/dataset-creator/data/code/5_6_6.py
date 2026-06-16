import inspect
class MROAnalyzer:
    def get_mro(self, cls):
        return list(cls.__mro__)
    def compare_hierarchies(self, class_a, class_b):
        mro_a = self.get_mro(class_a)
        mro_b = self.get_mro(class_b)
        common_prefix_len = 0
        for i in range(min(len(mro_a), len(mro_b))):
            if mro_a[i] == mro_b[i]:
                common_prefix_len += 1
            else:
                break
        diff_points = []
        max_mro_len = max(len(mro_a), len(mro_b))
        for i in range(max_mro_len):
            val_a = mro_a[i] if i < len(mro_a) else None
            val_b = mro_b[i] if i < len(mro_b) else None
            if val_a != val_b:
                diff_points.append({
                    'index': i,
                    'class_a_mro_at_index': val_a,
                    'class_b_mro_at_index': val_b
                })
        return {
            'mro_class_a': mro_a,
            'mro_class_b': mro_b,
            'common_prefix_length': common_prefix_len,
            'first_divergence_point': diff_points[0] if diff_points else None,
            'total_differences': len(diff_points)
        }
def create_sample_classes():
    class BaseA:
        def method(self):
            return "Base A"
    class Middle1(BaseA):
        pass
    class TopA(Middle1):
        def override_method(self):
            return "Top A Override"
    class BaseB:
        def method(self):
            return "Base B"
    class Middle2(BaseB):
        pass
    class TopB(Middle2, BaseA):
        def override_method(self):
            return "Top B Override"
    return TopA, TopB
if __name__ == '__main__':
    cls_a, cls_b = create_sample_classes()
    analyzer = MROAnalyzer()
    result = analyzer.compare_hierarchies(cls_a, cls_b)
    print("Method Resolution Order for Class A:")
    [print(f"  {i}: {cls}") for i, cls in enumerate(result['mro_class_a'])]
    print("\nMethod Resolution Order for Class B:")
    [print(f"  {i}: {cls}") for i, cls in enumerate(result['mro_class_b'])]
    print(f"\nCommon Prefix Length: {result['common_prefix_length']}")
    if result['first_divergence_point']:
        divergence = result['first_divergence_point']
        print(f"First Divergence at Index {divergence['index']}:")
        print(f"  Class A has: {divergence['class_a_mro_at_index']}")
        print(f"  Class B has: {divergence['class_b_mro_at_index']}")
    print(f"\nTotal Differences in Hierarchy: {result['total_differences']}")