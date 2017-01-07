# Base program for a BMI calculator and exercise planner. Simply enter your
# weight and height, and the program, based on your BMI, prints out an
# exercise routine.

def main():
    # Declare variables
    x = eval(input("Whats your weight(kg)? "))
    z = eval(input("And your height(m)? "))
    global a
    # Calculate BMI
    a=x/(z*z)
    #print("\n")
    if a<18.5:
        low()
    elif 18.5<=a<=24.9:
        normal()
    elif 25<=a<=29.9:
        high()
    else:
        print ("You're BMI seeems too high, we highly recommend visiting a doctor")

    
def low(): # if BMI is low
    print ("%.2f is a" %a, "low BMI.")
    print ("Eat between 2000-2500 calories a day")
    print ("DAILY WORKOUT - 30 squats, 20 lunges, 10 push-ups, 25 triceps dips, 25 sit-ups, 45 seconds plank") 
    print ("repeat 3-4 times")
    import urllib, cStringIO  
    
def normal(): # if BMI is normal
    print ("%.2f is a" %a, "normal BMI.")
    print ("Great job! Continue eating the same number of calories")
    print ("DAILY WORKOUT - 20 high-knees in place, 25 squats, 25 lunges,")
    print ("10 second side plank each side, 15 leg raises, 15 second plank")
    print ("Repeat 3-4 times")
    
def high(): # if BMI is high
    print ("%.2f is a" %a, "high BMI.")
    print ("We need to get some work done. LET'S GET IT!")
    print ("Eat between 1600-1800 calories per day.")
    print ("DAILY WORKOUT - 20 high-knees in place, 1 minute jump rope, 12 squats, 12 lunges, 10 sit-ups, 20 second plank")
    print ("Repeat 3-4 times")

main()
