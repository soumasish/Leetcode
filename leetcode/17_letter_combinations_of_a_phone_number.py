"""Created by sgoswami on 7/5/17."""
"""Given a digit string, return all possible letter combinations that the number could represent."""
import collections


class Solution(object):
    def __init__(self):
        self.digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combinations = set()
        return self.helper(digits, '', combinations)

    def helper(self, digits, path, combinations):
        if not digits:
            combinations.add(path)
            return
        curr, rest = digits[0], digits[1:]
        letters = self.digit_map[curr]
        for letter in letters:
            self.helper(digits, path+letter, combinations)
        return combinations


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))