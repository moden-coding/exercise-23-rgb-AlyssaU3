#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    
    with open(filename, "r") as a:

        final=[]
        
        for line in a.readlines():
            
            
                    colors=re.match(r"^\s*(\d+)\s+(\d+)\s+(\d+)[ \t]+(.+)$", line)
               #print(colors)
                    if colors:
                        red, green, blue, name = colors.groups()
                        final.append(f"{red}\t{green}\t{blue}\t{name}")
        return(final)

    


def main():
     result = red_green_blue()
     print(result)
    #red_green_blue()

    #print(f"The result should be a list, it is a {type(result)}
    #print(f"The length of the list should be 753, was {len(result)}   

    #for s in result:
    #      if(type(s) != str):
    #            print("All items in the list should be strings")
    #   
       
    #for i, s in enumerate(result):
    #    pos = "in result list with index %i: %s" % (i, s)
    #    t=s.split("\t")
    #    r=int(t[0])
    #    g=int(t[1])
    #    b=int(t[2])
    #    name=t[3]   
    #    if(r < 0 or r > 255):
    #        print("The value of the red component should be in the range [0,255] %s!" % pos)
    #    if(g < 0 or g > 255):
    #        print("The value of the green component should be in the range [0,255] %s!" % pos)
    #    if(b < 0 or b > 255):
    #        print("The value of the blue component should be in the range [0,255] %s!" % pos)

    #    t = result[1].split("\t")
    #    r=int(t[0])
    #    g=int(t[1])
    #    b=int(t[2])
    #    name=t[3]
    #    if r != 248:
    #        print("Incorrect value of red component in the second string!"
    #    if g != 248:
    #        print("Incorrect value of green component in the second string!"
    #    if b != 255:
    #        print("Incorrect value of blue component in the second string!"
    #



if __name__ == "__main__":
    main()
