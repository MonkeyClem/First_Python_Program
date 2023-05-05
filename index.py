print("Welcome to my computer quiz :)")

playing = input("Do you want to play ? ")
print (playing)

if playing.lower() != "yes":
        quit()

print("Okay! Let's play :) ")

answer = input ("What does F.B.I stand for ? ")
if answer.lower() == "federal bureau of investigation":
        print("Correct !")
else : print("INCORRECT !!!")

answer = input ("What does B.A.C stand for ? ")
if answer.lower() == "brigade anti criminalité":
        print("Correct !")
else : print("INCORRECT !!!")

answer = input ("What does P.J stand for ? ")
if answer.lower() == "police judiciaire":
        print("Correct !")
else : print("INCORRECT !!!")

answer = input ("What does U.F.C stand for ? ")
if answer.lower() == "ultimate fighting championship":
        print("Correct !")
else : print("INCORRECT !!!")