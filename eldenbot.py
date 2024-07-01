
import win32gui 
import time
from win32_helper import Win32Helpers

target_window = "ELDEN RING™"
timeout_limit = 10
counter = 0

#Key bindings
use_item_button = "r"
walk_forward_button = "w"
walk_left_button = "a"
weapon_skill_button = "1" #change yours ingame to 1 or a single button. 
open_map_button = "g"
map_open_sites_of_grace_page = "f"
select_site_button = "e"
escape_button = "esc"

def get_current_window_name(): #this function returns the name of the window thats in focus.
    window_t = Win32Helpers.get_active_window()
    current_window_name = win32gui.GetWindowText(window_t)
    return current_window_name    

def use_item(delay): #this function uses an item. I use my cracked twiggy tear phyics
    Win32Helpers.press(use_item_button)  
    time.sleep(delay)

def run_straight(run_straight_time):
    Win32Helpers.press(walk_forward_button) #Ive found this helps alight the character sometimes. Might not be necessary tho
    Win32Helpers.pressAndHold(walk_forward_button)
    time.sleep(run_straight_time)
    Win32Helpers.release(walk_forward_button)

def run_angle(angle_time):
    Win32Helpers.pressAndHold(walk_forward_button, walk_left_button) #walk sideways by pressing both a and w
    time.sleep(angle_time)
    Win32Helpers.release(walk_forward_button,walk_left_button)
    

def attack(delay):
    Win32Helpers.press(weapon_skill_button) # I rebinded ash of war skill to 1 instead of default shift + click
    time.sleep(delay) #Give enough time for all the albinuarics to die

def return_to_grace(delay): # delay is such that the game can catch up
    Win32Helpers.press(open_map_button)
    time.sleep(delay)
    Win32Helpers.press(map_open_sites_of_grace_page)
    time.sleep(delay)  
    Win32Helpers.press(select_site_button) 
    time.sleep(delay)
    Win32Helpers.press(select_site_button)
    time.sleep(delay)
    Win32Helpers.press(escape_button) #sometimes useful to escape from map in case something goes wrong.
    time.sleep(delay)


#code starts here
while counter < timeout_limit:
    
    time.sleep(1) 

    current_window_name= get_current_window_name()

    if current_window_name == target_window: # triggers while elden ring is the focused window
        counter = 0
        msg = target_window+ " is in focus"
        print(msg)
        run_counter = 0

        # Be at Palace Approach Ledge Road Site of Grace
        time.sleep(3)
        return_to_grace(0.6)
        time.sleep(5)
        # ^This will reset the charactar and camera angle

        while current_window_name == target_window: # Execute the run, breaks loop when elden ring is not in focus
            ####################################################
            run_counter = run_counter+1
            msg = "Run #" + str(run_counter)
            print(msg) 

            use_item(2) # I use the physics flask with the cracked twiggy tear in case something happens overnight, the runes wont be lost
            run_straight(3.1) 
            run_angle(2.4)
            time.sleep(0.5) 
            attack(8) #eight seconds for skill to execute and kill
            return_to_grace(0.3)
            time.sleep(6) #lets all the loading occur prior to starting again
            ####################################################
            if run_counter % 10 == 0: #evey ten runs we wait an additional 5 seconds to account for time differences between game and code
                print("Reset Position") # lowers rune amount by a little but makes the code run all night with very little issues. Its more of a peace of mind thing.
                time.sleep(5)

            current_window_name= get_current_window_name() 


    else: #if Elden Ring is not the active window then there will be a 10 second countdown to exit
        time_remaining = timeout_limit - counter
        msg = "Window not found, timeout in " + str(time_remaining)
        print(msg)

    counter = counter +1
        



  


