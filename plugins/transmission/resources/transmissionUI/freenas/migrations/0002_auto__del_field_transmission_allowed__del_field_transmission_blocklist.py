# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Transmission.allowed'
        db.delete_column('freenas_transmission', 'allowed')

        # Deleting field 'Transmission.blocklist'
        db.delete_column('freenas_transmission', 'blocklist')


        # Changing field 'Transmission.global_seedratio'
        db.alter_column('freenas_transmission', 'global_seedratio', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2))

    def backwards(self, orm):
        # Adding field 'Transmission.allowed'
        db.add_column('freenas_transmission', 'allowed',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Transmission.blocklist'
        db.add_column('freenas_transmission', 'blocklist',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Transmission.global_seedratio'
        db.alter_column('freenas_transmission', 'global_seedratio', self.gf('django.db.models.fields.IntegerField')())

    models = {
        'freenas.transmission': {
            'Meta': {'object_name': 'Transmission'},
            'dht': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'download_dir': ('django.db.models.fields.CharField', [], {'default': "'/usr/pbi/transmission-amd64/etc/transmission/home/Downloads'", 'max_length': '500'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'encryption': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'global_seedratio': ('django.db.models.fields.DecimalField', [], {'default': '2', 'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lpd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'peer_port': ('django.db.models.fields.IntegerField', [], {'default': '51413', 'blank': 'True'}),
            'peerlimit_global': ('django.db.models.fields.IntegerField', [], {'default': '240'}),
            'peerlimit_torrent': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'portmap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rpc_password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_port': ('django.db.models.fields.IntegerField', [], {'default': '9091', 'blank': 'True'}),
            'rpc_username': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_whitelist': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'utp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'watch_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']