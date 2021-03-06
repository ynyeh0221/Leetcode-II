class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == ' ':
                return len(s) - i - 1
            if i == 0:
                return len(s) - i
        return 0
