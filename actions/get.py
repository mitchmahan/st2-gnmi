from st2common.runners.base_action import Action
from pygnmi.client import gNMIclient


class GnmiGet(Action):
    """This runs a gnmi get operation on the remote network device.
    """

    def run(self, host, port, username, password, path, insecure=True):
        device = (host, port)
        with gNMIclient(target=device, username=username, password=password, insecure=insecure) as gc:
            self.logger.info("Successfully connected to device.")
            self.logger.info(f"Running gNMI get for {path}")
            result = gc.get(path=path)
        return result
