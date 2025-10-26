s="hello world"
print(s)
t="python"
print(t[0])
print(t[-1])
print("reversed text is ",t[::-1])
print(t.count("n"))
s="python is easy to lern"
print(s.replace(" ","_"))
w="malayalam"
p=(w[::-1])
print(p)
if w==p:
    print("palindrome",p)
else:
    print("not palindrom")

#try out all methods on string
g="programming_language"
print(g.upper())
print(g.lower())
print(g.capitalize())
print(g.title())
print(g.strip())
print(g.rstrip())
print(g.lstrip())
print(g.split(sep=None))
print(g.splitlines())
print(g.join("a,b,c"))
print(g)
print(g.replace("m","w"))
print(g)
print(g.find("a")) #returns index number of the given letter in the string
print(g.rfind("a"))
print(g.index("r"))
print(g.rindex("a"))
print(g.count("a"))
print(g.startswith("pro"))
print(g.startswith("programming"))
print(g.endswith("a"))
print(g.isalpha())
print(g.isdigit())
print(g.isspace())
print(g.isalnum())
print(g.swapcase())
print(g.center(50,"*"))
print(g.ljust(50,"#"))
print(g.rjust(50,"#"))
print(g.zfill(50))
print(g.partition("ing"))
print(g.rpartition("o"))
print(g.encode())
print(g.expandtabs(8))
print(g.isdecimal())
print(g.isnumeric())
print(g.isidentifier())
print(g.casefold())






