# Trie tree example
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.isend = False

    def insert(self, word):
        curr = self.root
        for i in word:
            curr = curr.children[i]
        curr.isend = True

    def search(self, word):
        curr = self.root
        for i in word:
            if curr.children.get(i, None):
                curr = curr.children[i]
            else:
                return False
        return curr.isend

    def start_with(self, word):
        curr = self.root
        for i in word:
            if curr.children.get(i):
                curr = curr.children[i]
            else:
                return False
        return True


# example
def main():
    word_list = []
    search_list = []
    start_with_list = []


# -----creat tree------

    root = Trie()
    for i in word_list:
        root.insert(i)
    # Trie has been built now
# ---------------------

# ---search example----
    search_res = []
    for i in search_list:
        if root.search(i):
            search_res.append(True)
        else:
            search_res.append(False)
    # result are is now save in search_res
# ---------------------

# -start_with example--
    start_with_res = []
    for i in search_list:
        if root.start_with(i):
            start_with_res.append(True)
        else:
            start_with_res.append(False)
    # result are is now save in start_with_res
# ---------------------


if __name__ == "__main__":
    main()
