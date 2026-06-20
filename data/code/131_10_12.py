class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

def entropy(labels):
    from collections import Counter
    counts = Counter(labels)
    total = len(labels)
    return -sum(count / total * (count / total) for count in counts.values())

def information_gain(left_labels, right_labels):
    left_entropy = entropy(left_labels)
    right_entropy = entropy(right_labels)
    total_samples = len(left_labels) + len(right_labels)
    return entropy([*left_labels, *right_labels]) - ((len(left_labels) / total_samples) * left_entropy + (len(right_labels) / total_samples) * right_entropy)

def split_data(data, labels, feature_index, threshold):
    left_data, left_labels, right_data, right_labels = [], [], [], []
    for x, y in zip(data, labels):
        if x[feature_index] <= threshold:
            left_data.append(x)
            left_labels.append(y)
        else:
            right_data.append(x)
            right_labels.append(y)
    return left_data, left_labels, right_data, right_labels

def build_tree(data, labels, depth=0, max_depth=None):
    if not data or not labels or (max_depth is not None and depth >= max_depth):
        from collections import Counter
        most_common = Counter(labels).most_common(1)
        return DecisionTreeNode(label=most_common[0][0])
    
    best_feature, best_threshold = None, float('inf')
    for feature_index in range(len(data[0])):
        thresholds = sorted(set(x[feature_index] for x in data))
        for threshold in thresholds:
            left_labels, right_labels = [y for _, y in split_data(data, labels, feature_index, threshold)]
            gain = information_gain(left_labels, right_labels)
            if gain < best_threshold:
                best_feature, best_threshold = feature_index, threshold
    
    left_data, left_labels, right_data, right_labels = split_data(data, labels, best_feature, best_threshold)
    left_tree = build_tree(left_data, left_labels, depth + 1, max_depth)
    right_tree = build_tree(right_data, right_labels, depth + 1, max_depth)
    
    return DecisionTreeNode(feature=best_feature, threshold=best_threshold, left=left_tree, right=right_tree)

def classify(tree, x):
    if tree.label is not None:
        return tree.label
    if x[tree.feature] <= tree.threshold:
        return classify(tree.left, x)
    else:
        return classify(tree.right, x)

if __name__ == '__main__':
    data = [
        [2.3, 1.7], [1.9, 0.8], [3.1, 2.5], [2.4, 1.6], [1.8, 0.9],
        [4.2, 3.0], [3.8, 2.9], [4.7, 3.5], [4.5, 3.2], [4.0, 2.8],
        [0.6, 0.4], [0.8, 0.5], [1.2, 0.7], [1.0, 0.6], [0.9, 0.5],
        [3.4, 2.1], [3.2, 1.9], [3.5, 2.2], [3.3, 2.0], [3.6, 2.3]
    ]
    labels = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1]
    
    tree = build_tree(data, labels)
    print(classify(tree, [2.5, 1.8]))