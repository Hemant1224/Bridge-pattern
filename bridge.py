# Abstraction (Bridge)
class Device:
    def __init__(self, implementor):
        self.implementor = implementor

    def toggle_power(self):
        if self.implementor.is_enabled():
            self.implementor.disable()
        else:
            self.implementor.enable()

# Refined Abstraction
class TV(Device):
    def watch_channel(self, channel):
        print(f"Watching channel {channel}")

# Implementor
class DeviceImplementor:
    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

# Concrete Implementor
class RemoteControl(DeviceImplementor):
    def __init__(self):
        self.is_on = False

    def is_enabled(self):
        return self.is_on

    def enable(self):
        self.is_on = True
        print("Remote control enabled")

    def disable(self):
        self.is_on = False
        print("Remote control disabled")

# Usage
tv = TV(RemoteControl())
tv.toggle_power()  # Remote control enabled
tv.watch_channel(42)  # Watching channel 42
tv.toggle_power()  # Remote control disabled
