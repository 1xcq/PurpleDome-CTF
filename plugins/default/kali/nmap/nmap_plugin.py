#!/usr/bin/env python3

# A plugin to nmap targets

from plugins.base.kali import KaliPlugin


# TODO All scan patterns need explicit logging into the attack log !
# TODO: Add config for subnet range for ping sweeps
# TODO: Add IP exclusion --exclude ip,ip,ip to not accidentially scan non-targets
# TODO: host discovery Ping scan: -sn
# TODO: host discovery PE ICMP echo
# TODO: host discovery PP ICMP timestamp
# TODO: host discovery PM ICMP netmask request
# TODO: host discovery PS: SYN host discovery
# TODO: host discovery PA: ACK host discovery
# TODO: host discovery PU: UDP host discovery
# TODO: host discovery PR: ARP ping
# TODO: host discovery -PO1: ICMP ping
# TODO: host discovery -PO2: IGMP ping
# TODO: --traceroute in addition to host discovery
# TODO: -R <ip> reverse DNS. Needs a DNS in the big picture. No idea if valuable
# TODO: host discovery reverse DNS resolution
# TODO OS identification
# TODO service discovery
# TODO stealth scans
# TODO firewall evasion
# TODO service fingerprinting
# TODO udp scans   -sU
# TODO TCP SYN scan: -sS
# TODO TCP connect scan: -sT
# TODO port scan without prior ping (this is to avoid triggering firewall logic): -Pn
# TODO: -O OS detection
# TODO: -sV service version detection
# TODO -sS syn scan, stealthy
# TODO -sT tcp connect scan - needs no special permissions
# TODO. -p- scan all ports
# TODO: -p <range> scan port rance

class NmapPlugin(KaliPlugin):

    # Boilerplate
    name = "nmap"
    description = "NMap scan the target"
    ttp = "T1595"
    references = ["https://attack.mitre.org/techniques/T1595/"]

    required_files = []    # Files shipped with the plugin which are needed by the kali tool. Will be copied to the kali share

    def __init__(self):
        super().__init__()
        self.plugin_path = __file__

    def command(self, targets, config):
        """ Generate the command (having a separate step assists on debugging)

        @param targets: A list of targets, ip addresses will do
        @param config:  dict with command specific configuration
        """

        # Set defaults if not present in config
        self.process_config(config)
        playground = self.machine_plugin.get_playground()

        # Generate command
        cmd = f"cd {playground};"
        # cmd += "sudo apt -y install nmap;"
        for t in targets:
            cmd += f"nmap {t};"

        return cmd

    def run(self, targets, config):
        """ Run the command

        @param targets: A list of targets, ip addresses will do
        @param config:  dict with command specific configuration
        """

        res = ""

        cmd = self.command(targets, config)

        res += self.run_cmd(cmd) or ""

        return res
