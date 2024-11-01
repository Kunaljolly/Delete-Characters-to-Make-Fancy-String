class Solution:
    def makeFancyString(self, s: str) -> str:
        s += "12"
        t = ""
        for x in range(len(s)-2):
            if s[x] == s[x+1] and s[x+1] == s[x+2]:
                continue
            else:
                t += s[x]
        return t
