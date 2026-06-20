class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

def gini_impurity(labels):
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    return 1 - np.sum(probabilities ** 2)

def split_data(X, y, feature, threshold):
    left_mask = X[:, feature] < threshold
    right_mask = ~left_mask
    return X[left_mask], y[left_mask], X[right_mask], y[right_mask]

def best_split(X, y):
    best_gini = float('inf')
    best_feature = None
    best_threshold = None
    for feature in range(X.shape[1]):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_y, right_y = y[X[:, feature] < threshold], y[X[:, feature] >= threshold]
            gini = len(left_y) * gini_impurity(left_y) + len(right_y) * gini_impurity(right_y)
            if gini < best_gini:
                best_gini = gini
                best_feature = feature
                best_threshold = threshold
    return best_feature, best_threshold

def build_tree(X, y, max_depth=None, depth=0):
    if len(np.unique(y)) == 1 or (max_depth is not None and depth >= max_depth):
        return DecisionTreeNode(label=np.unique(y)[0])
    feature, threshold = best_split(X, y)
    left_X, left_y, right_X, right_y = split_data(X, y, feature, threshold)
    left_node = build_tree(left_X, left_y, max_depth, depth + 1)
    right_node = build_tree(right_X, right_y, max_depth, depth + 1)
    return DecisionTreeNode(feature=feature, threshold=threshold, left=left_node, right=right_node)

def predict(tree, x):
    current_node = tree
    while current_node.label is None:
        if x[current_node.feature] < current_node.threshold:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return current_node.label

if __name__ == '__main__':
    import numpy as np
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20],
                  [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [35, 36], [37, 38]])
    y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    tree = build_tree(X, y)
    print(predict(tree, np.array([25, 26])))