class SubfieldsInAI:
    def Subfields():
        print('Sub-fields in AI are:\nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing')

class OddEven:
    def OddEven():
            value = int(input("Enter a number:"))
            if(value%2 == 0):
                print(value,"is Even number")
            else:
                print(value,"is Odd number")

class ElegiblityForMarriage:
    def Elegible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        
        if(gender.startswith('m') or gender.startswith('M')):
            if(age < 21):
                print(age, 'is not eligiable for gender - ',gender)
            else:
                print(age, 'is eligiable for gender - ',gender)
        elif(gender.startswith('f') or gender.startswith('F')):
            if(age < 18):
                print(age, 'is not eligiable for gender - ',gender)
            else:
                print(age, 'is eligiable for gender - ',gender)
        else:
            print('Please give either MALE or FEMALE as gender')       

class FindPercent:
    def percentage():
        Subject1= 23
        Subject2= 45
        Subject3= 34
        Subject4= 23
        Subject5= 23
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        print('Total :', total)
        print('Percentage :', total/5)

class triangle:
    def triangle():
        Height=3
        Breadth=4
        area_formula = (Height*Breadth)/2
        print('Area of Triangle:',area_formula)
        Height1=3
        Height2=4
        Breadth=45
        perimeter_formula= Height1+Height2+Breadth
        print('Perimeter of Triangle:',perimeter_formula)   